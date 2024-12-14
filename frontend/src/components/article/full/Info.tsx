import { article } from 'types'
import { Progress } from 'components/ui/progress'
import { get_date, stock_change_color } from 'lib/utils'

const Info = ({ article }: { article: article }) => {
  return (
    <div className="flex justify-between gap-5 border-b-2 border-t-2 py-4">
      <div>
        <p className="text-xl font-bold">{article.authors.join(' • ')}</p>
        <p className="text-xl">{get_date(article.created_at)}</p>
      </div>
      <div className="w-1/3">
        <p className="text-lg font-bold">Sentiment:</p>
        <Progress value={(article.sentiment_compound[0] + 1) * 50} />
      </div>
      {article.stocks_changes_name?.length > 0 && (
        <div className="flex flex-wrap justify-end gap-2">
          {article.stocks_changes_name?.map((stock, i) => (
            <div key={i} className="flex flex-col text-xl">
              <p className="text-lg font-bold">{stock}</p>
              <p style={{ color: stock_change_color(article.stocks_changes_value[i]) }}>
                {article.stocks_changes_value[i] > 0 ? '+' : ''}
                {article.stocks_changes_value[i]}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default Info
