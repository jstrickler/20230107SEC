from dataclasses import dataclass, field, fields

@dataclass
class President:
    term: int = field(metadata={'abc': 25})
    first_name: str = None
    last_name: str = None

if __name__ == '__main__':
    p = President(1, 'George', 'Washington')
    print(p)
    print(p.term)
    print(fields(p)[0].metadata['abc'])
