import webbrowser
import config


def get_access_token():
    if config.APP_ID == '':
        raise Exception('Приложение не зарегестрированно.')
    params = ','.join(config.PARAMS)

    url = f'https://oauth.vk.com/authorize?client_id={config.APP_ID}' \
          f'&redirect_uri=https://oauth.vk.com/blank.hmtl&scope={params}' \
          f'&response_type=token' \
          f'&display=page'
    webbrowser.open_new_tab(url)


if __name__ == "__main__":
    get_access_token()