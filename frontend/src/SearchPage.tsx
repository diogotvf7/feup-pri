import logo from './logo.svg'
import { Input } from 'src/components/ui/input'
import { useEffect, useState } from 'react'
import { Article } from 'src/types'
import ArticlePreview from './components/ArticlePreview'

const urlParams = (query: string) =>
  new URLSearchParams({
    q: query,
    defType: 'edismax',
    qf: 'title^3 body^2 authors',
    pf: 'title^3 author^2 body',
    fl: '*',
    'q.op': 'AND',
    indent: 'true',
    rows: '10',
  })

function SearchPage() {
  const [articles, setArticles] = useState([])
  const [query, setQuery] = useState('')

  const fetchData = async () => {
    try {
      const response = await fetch(`http://localhost:8983/solr/stocks/select?${urlParams(query)}`, {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      })

      if (!response.ok) console.log(response.statusText)
      const data = await response.json()

      console.log(`http://localhost:8983/solr/stocks/select?${urlParams(query)}`, data.response.docs)
      setArticles(data.response.docs)
      console.log('articles: ', articles)
    } catch (error) {
      console.error(error)
    }
  }

  useEffect(() => {
    fetchData()
    console.log(articles)
  }, [query])

  return (
    <div className="h-screen bg-stone-800">
      <header className="flex h-max items-center justify-between border-b-2 border-stone-900 p-4">
        <a href="/" className="">
          <img src={logo} alt="logo" />
        </a>
        <Input
          type="text"
          className="max-w-[584px] bg-stone-300 px-5"
          onChange={(event) => setQuery(event.target.value)}
        />
      </header>
      <main className="m-5 flex h-full flex-col items-center justify-start gap-5 overflow-y-scroll text-stone-200">
        {articles.map((article: Article) => (
          <ArticlePreview article={article} key={article.id} />
        ))}
      </main>
    </div>
  )
}

export default SearchPage
