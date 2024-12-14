import React from 'react'
import { article } from 'types'
import Full from './full'
import Preview from './Preview'

const Article = ({ article, type }: { article: article; type: string }) => {
  if (type == 'full') return <Full article={article} />
  else if (type == 'preview') return <Preview article={article} />
  return <div>Error!</div>
}

export default Article
