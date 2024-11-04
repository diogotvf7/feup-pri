from datetime import datetime, timezone

class Article:
    def __init__(self, title, created_at, body, stocks_changes=None, authors=None):
        self.title = title
        
        if isinstance(created_at, str):
            self.created_at = datetime.strptime(created_at, '%d/%m/%Y')
        elif isinstance(created_at, datetime):
            self.created_at = created_at
        else:
            raise ValueError("created_at must be a string in 'dd/mm/yyyy' format or a datetime object.")

        self.body = body
        self.stocks_changes = stocks_changes
        self.author = authors

    def to_dict(self):
        created_at_iso = self.created_at.astimezone(timezone.utc).isoformat() + 'Z'
        #TODO: NEed to change we create stocks_changes
        filtered_dict = {
            'title': self.title,
            'authors': self.author,
            'created_at': created_at_iso,
            'body': self.body,
            'stocks_changes': self.stocks_changes
        }
        return {key: value for key, value in filtered_dict.items() if value is not None}
