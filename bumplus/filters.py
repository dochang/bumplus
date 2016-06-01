def strftime(value, format='%x'):
    return value.strftime(format)

filters = {
    'strftime': strftime,
}
