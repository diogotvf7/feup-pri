import logo from "./logo.svg";
import { Input } from "src/components/ui/input";
import { useEffect, useState } from "react";

import axios from 'axios';


type Document = {
  title: string
  authors: Array<string>
  created_at: Array<string>
  body: string
  stocks_changes_name: Array<string>  
  stocks_changes_value: Array<number>  
  sentiment_compound: number
  id: number  
  score: number
  _version_: number  
  _root_: string  
}

const get_query = (query : string) => ({
  query: query,
  params: {
    defType: "edismax",
    qf: "title^3 body^2 authors",
    pf: "title^3 author^2 body",
    fl: "id,score",
    "q.op": "AND",
    indent: "true",
    rows: 10,
  }
})

const urlParams = (query : string) => new URLSearchParams({
  q: query,
  defType: "edismax",
  qf: "title^3 body^2 authors",
  pf: "title^3 author^2 body",
  fl: "id,score",
  "q.op": "AND",
  indent: "true",
  rows: "10"
});

function SearchPage() {
  const [documents, setDocuments] = useState([])
  const [query, setQuery] = useState("")
  

  const fetchData = async () => {
    try {

        const response = await fetch(`http://localhost:8983/solr/stocks/select?${urlParams(query)}`, {
          method: "GET",
          headers: {
              Accept: "application/json",
          },
        });

        if (!response.ok) console.log("Fodeu!");
        const data = await response.json();
        
        setDocuments(data.response.docs)
    } catch (error) {
        console.error(error)
    }
  }
  
  useEffect(() => {
    // console.log(get_query(query));
    fetchData()
  }, [query])
  
  return (
    <div className="bg-stone-800 h-screen">
      <header className="flex justify-start px-4 border-b-2 border-stone-900 h-max">
        <a
          href="/"
          className=""
        >
          <img src={logo} alt="logo" />
        </a>
      </header>
      <main className="flex flex-col items-center h-full justify-center p-auto">
        <Input type="text" className="max-w-[584px] bg-stone-300 rounded-full px-5" onChange={event => setQuery(event.target.value)} />
        <div className="results">
          {documents.map((document: Document) => (
              <div key={document.id}>
                <p>{document.score}</p>
              </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default SearchPage;
