import { useLocation } from 'react-router-dom'
import { article } from 'types'
import logo_full from 'assets/logo-full.svg'
import { stock_change_color, get_date } from 'lib/utils'
import { Progress } from 'components/ui/progress'
import Article from '../components/article'

const ArticlePage = () => {
  const location = useLocation()
  const article = location.state?.article as article | undefined

  return (
    <div className="flex h-screen flex-col bg-stone-800">
      <header className="flex h-max items-center justify-between border-b-2 border-stone-900 p-4">
        <a href="/">
          <img src={logo_full} alt="logo" />
        </a>
      </header>
      <main className="flex flex-grow flex-col items-center gap-5 overflow-auto text-stone-200">
        {article ? (
          <Article article={article} type="full" />
        ) : (
          <div className="">
            <h1 className="text-8xl font-extrabold">Oops!</h1>
            <h2 className="text-3xl">Article not found</h2>
          </div>
        )}
      </main>
    </div>
  )
}

export default ArticlePage
