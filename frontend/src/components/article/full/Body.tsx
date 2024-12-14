import { article } from 'types'
import { split_paragraphs } from '../../../lib/utils'

const Body = ({ article }: { article: article }) => {
  const paragraphs = split_paragraphs(article.body)

  return (
    <>
      {paragraphs?.map((p, i) => (
        <p key={i} className="my-4 text-2xl">
          {p}
        </p>
      ))}
    </>
  )
}

export default Body
