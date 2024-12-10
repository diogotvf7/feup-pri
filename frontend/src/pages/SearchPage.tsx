import logo from 'assets/logo.svg'
import logo_full from 'assets/logo-full.svg'
import { useEffect, useState } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { article } from 'types'
import { Input } from 'components/ui/input'
import Article from '../components/article'

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

const SearchPage = () => {
  const [articles, setArticles] = useState([])
  const [query, setQuery] = useState('')
  const navigate = useNavigate()
  const [searchParams, _] = useSearchParams()

  /**
   * This function is used to fetch articles from the Solr server.
   */
  const fetchData = async (searchQuery: string) => {
    try {
      const response = await fetch(`http://localhost:8983/solr/stocks/select?${urlParams(searchQuery)}`, {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      })

      if (!response.ok) console.log(response.statusText)
      const data = await response.json()

      setArticles(data?.response?.docs)
    } catch (error) {
      console.error(error)
    }
  }

  /**
   * This useEffect is used to fetch articles when the query changes.
   */
  useEffect(() => {
    fetchData(query)
  }, [query])

  /**
   * This useEffect is used to recover the query when the page is refreshed or when the user navigates back to the page.
   */
  useEffect(() => {
    const queryParam = searchParams.get('q') || ''
    setQuery(queryParam)

    if (queryParam) {
      fetchData(queryParam)
    } else {
      setArticles([])
    }
  }, [searchParams])

  /**
   * Only update the URL when the user leaves the input field.
   * This is to prevent the URL from updating on every keystroke.
   */
  const handleBlur = () => {
    navigate(`/search?q=${query}`)
  }

  return (
    <div className="flex h-screen flex-col bg-stone-800">
      <header className="flex items-center justify-between border-b-2 border-stone-900 p-4">
        <a href="/" className="">
          <img src={logo_full} alt="logo" />
        </a>
        <Input
          type="text"
          className="max-w-[584px] bg-stone-300 px-5"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search stock news here!"
          onBlur={handleBlur}
          autoFocus
        />
      </header>
      <main className="m-7 flex flex-grow flex-col items-center gap-5 overflow-auto text-stone-200">
        {query && articles.length > 0 ? (
          articles.map((article: article) => <Article article={article} type="preview" key={article.id} />)
        ) : query ? (
          <div className="flex animate-pulse flex-col items-center">
            <img src={logo} alt="logo" className="size-72 flex-grow" />
            <p className="text-6xl font-extrabold">Oops!</p>
            <p className="text-4xl font-bold">No articles found...</p>
          </div>
        ) : (
          <div className="flex animate-pulse flex-col items-center">
            <img src={logo} alt="logo" className="size-72 flex-grow" />
            <p className="text-4xl font-bold">Search something!</p>
          </div>
        )}
      </main>
    </div>
  )
}

export default SearchPage
