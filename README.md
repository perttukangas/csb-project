# Tietoturvan perusteet: Project I

LINK: https://github.com/Perttu-Kangas/csb-project

This project uses OWASP 2021 list.

Make sure you have Python and Django installed. App can be started with `python3 manage.py runserver`.

## Installation

1. Clone repo
2. Go to cloned repo folder in terminal
3. Start the app by `python3 manage.py runserver`
4. Log in using username `alice` and password `redqueen`

## FLAW 1: Broken Access Control

exact source link pinpointing flaw 1...
description of flaw 1...
how to fix it...

reviews/<user id> can be accessed by anyone

## FLAW 2: Cross-Site Request Forgery (CSRF)

exact source link pinpointing flaw 2...
description of flaw 2...
how to fix it...

review post doesn't include csrf token

## FLAW 3: Injection (Cross-Site Scripting (XSS))

reviews.html

## FLAW 4: Cryptographic Failures

secret key in git, debug is true, dev database is in git

## FLAW 5: Identification and Authentication Failures

simple session
