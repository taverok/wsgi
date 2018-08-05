from simple import router


@router.route('/test', method=["GET"])
def test():
    return 'test page', {}, 200
