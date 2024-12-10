import React from 'react'
import { Article } from '../types'
import TimeAgo from 'javascript-time-ago'
import en from 'javascript-time-ago/locale/en'

const MAXLEN = 300

const ArticlePreview = ({ article }: { article: Article }) => {
  TimeAgo.addLocale(en)
  const timeAgo = new TimeAgo('en-US')

  return (
    <div className="w-1/2 text-base">
      <div className="flex justify-between">
        <p>{article.authors.join(', ')}</p>
        <p>{timeAgo.format(new Date(article.created_at))}</p>
      </div>
      <a href="/" className="text-xl font-extrabold">
        <h1>{article.title}</h1>
      </a>
      <p className="line-clamp-2 text-ellipsis">{article.body.substring(0, MAXLEN)}</p>
    </div>
  )
}

export default ArticlePreview
