import Title from './Title'
import Info from './Info'
import Body from './Body'

import { article } from 'types'

const Article = ({ article }: { article: article }) => {
  return (
    <div className="w-1/2 text-2xl">
      <Title article={article} />
      <Info article={article} />
      <Body article={article} />
    </div>
  )
}

export default Article
