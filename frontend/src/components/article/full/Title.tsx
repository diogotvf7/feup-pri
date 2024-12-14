import React from 'react'
import { article } from '../../../types'

const Title = ({ article }: { article: article }) => {
  return <h1 className="my-4 text-4xl font-extrabold">{article.title}</h1>
}

export default Title
