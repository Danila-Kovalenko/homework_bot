class RESPONSE_ERROR:
    def __init__(self) -> None:
        self.RESPONSE_ERROR = ('Отказ от обслуживания: {error}, key {key}. '
                               'endpoint: {url}, headers: {headers},'
                               'params: {params}')


class API_ANSWER_ERROR:
    def __init__(self) -> None:
        self.API_ANSWER_ERROR = ('Ошибка подключения к API: {error}. '
                                 'endpoint: {url}, headers: {headers},'
                                 ' params: {params}')


class STATUS_CODE_ERROR:
    def __init__(self) -> None:
        self.STATUS_CODE_ERROR = ('Ошибка при запросе к API: '
                                  'status_code: {status_code},'
                                  'endpoint: {url}, '
                                  'headers: {headers}, params: {params}')


class UNKNOWN_STATUS_ERROR:
    def __init__(self) -> None:
        self.UNKNOWN_STATUS_ERROR = 'Неизвестный статус: {}'


class CHANGED_STATUS:
    def __init__(self) -> None:
        self.CHANGED_STATUS = 'Изменился статус проверки работы "{}". {}'


class SEND_MESSAGE_INFO:
    def __init__(self) -> None:
        self.SEND_MESSAGE_INFO = 'Отправлено сообщение: "{}"'


class RESPONSE_NOT_DICT:
    def __init__(self) -> None:
        self.RESPONSE_NOT_DICT = 'Ответ API не является словарем'


class HOMEWORKS_NOT_IN_RESPONSE:
    def __init__(self) -> None:
        self.HOMEWORKS_NOT_IN_RESPONSE = 'Отсутствует ключ homeworks'


class HOMEWORKS_NOT_LIST:
    def __init__(self) -> None:
        self.HOMEWORKS_NOT_LIST = 'Домашки приходят не в виде списка'


class TOKEN_NOT_FOUND:
    def __init__(self) -> None:
        self.TOKEN_NOT_FOUND = 'Токен {} не найден!'


class ERROR_MESSAGE:
    def __init__(self) -> None:
        self.ERROR_MESSAGE = 'Сбой в работе программы: {}'


class HOMEWORK_NAME_NOT_FOUND:
    def __init__(self) -> None:
        self.HOMEWORK_NAME_NOT_FOUND = 'Не найден ключ `homework_name`!'


class SEND_MESSAGE_ERROR:
    def __init__(self) -> None:
        self.SEND_MESSAGE_ERROR = 'Ошибка при отправке сообщения: {}'


class TOKEN_ERROR:
    def __init__(self) -> None:
        self.TOKEN_ERROR = 'Ошибка в токенах!'
