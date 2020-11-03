import re

from typing import Pattern


def get_cmp_url_re() -> Pattern[str]:
    # unicode letters range (must not be a raw string)
    ul = '\u00a1-\uffff'
    # host patterns
    hostname_re = fr'[a-z{ul}0-9](?:[a-z{ul}0-9-]{{0,61}}[a-z{ul}0-9])?'
    # max length for domain name labels is 63 characters
    domain_re = fr'(?:\.(?!-)[a-z{ul}0-9-]{{1,63}}(?<!-))*'
    tld_re = (
        r'\.'  # dot
        r'(?!-)'  # can't start with a dash
        fr'(?:[a-z{ul}-]{{2,63}}'  # domain label
        r'|xn--[a-z0-9]{1,59})'  # or punycode label
        r'(?<!-)'  # can't end with a dash
        r'\.?')  # may have a trailing dot

    return re.compile(
        fr'(?:({hostname_re}{domain_re}{tld_re}))'
        r'(?::\d{2,5})?'  # port
        r'(?:[/?#][^\s]*)?'  # resource path
        r'\Z', re.IGNORECASE)


URL_RE = get_cmp_url_re()


def is_url(url: str) -> bool:
    if URL_RE.search(url):
        return True
    return False


def main():
    assert is_url('http://yandex.ru/') is True
    assert is_url('yandex.ru') is True
    assert is_url('https://yandex.com/') is True
    assert is_url('https://\publ') is False
    assert is_url('https://news/dagestancy/1-0-11') is False
    assert is_url('javascript:void(0)') is False
    assert is_url('https://вечерний-екатеринбург.рф/') is True
    assert is_url('https://xn----8sbdbiiabb0aehp1bi2bid6az2e.xn--p1ai/') is True
    assert is_url('https://xn--e1aktc.xn--p1ai/') is True
    assert is_url('htps://xn--e1aktc.xn--p1ai/') is True
    print('OK!')


if __name__ == '__main__':
    main()
