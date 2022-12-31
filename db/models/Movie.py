from db.Model import ModelAbstract


class Movie(ModelAbstract):
    _fillable: tuple = (
        'title',
        'poster',
        'rate'
    )
