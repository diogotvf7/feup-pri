export type article = {
    title: string
    authors: Array<string>
    created_at: string
    body: string
    stocks_changes_name: Array<string>  
    stocks_changes_value: Array<number>  
    sentiment_compound: Array<number>
    id: number  
    score: number
    _version_: number  
    _root_: string  
}