import { article } from 'types'
import TimeAgo from 'javascript-time-ago'
import en from 'javascript-time-ago/locale/en'
import { Link } from 'react-router-dom'
import { article_to_url } from 'lib/utils'

const MAXLEN = 300

const Preview = ({ article }: { article: article }) => {
  TimeAgo.addLocale(en)
  const timeAgo = new TimeAgo('en-US')
  const url = article_to_url(article)

  return (
    <article className="w-1/2 text-base">
      <div className="flex justify-between">
        <p>
          By <strong>{article.authors.join(', ')}</strong>
        </p>
        <p>{timeAgo.format(new Date(article.created_at))}</p>
      </div>
      <Link to={`/article/${url}`} state={{ article }} className="text-xl font-extrabold text-blue-300">
        <h1>{article.title}</h1>
      </Link>
      <p className="line-clamp-2 text-ellipsis">{article.body.substring(0, MAXLEN)}</p>
    </article>
  )
}

export default Preview
