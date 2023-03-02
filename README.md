# Tietoturvan perusteet: Project I

LINK: https://github.com/Perttu-Kangas/csb-project

This project uses OWASP 2021 list.

Make sure you have Python and Django installed.

## Installation

1. Clone repo
2. Go to cloned repo folder in terminal
3. Start the app by `python3 manage.py runserver`
4. Log in using username `alice` and password `redqueen`

## FLAW 1: Broken Access Control

#### Exact source

- INSERT LINK

#### Description

The review route gets user id as parameters when doing GET request to `review/<user id>`. However this route doesn't have login required, and it also allows everyone to see other user's received and given reviews, which should be hidden from others than participants of the review. Meaning by simply changing the user id anyone can see every review.

#### How to fix it

This flaw can be fixed by first making the route require login to access. Then the route should be changed to just `review/`. After that the user should be fetched from request, and not from the url.

Links to fixes:
- Fix login required: INSERT LINK
- Fix user fetch: INSERT LINK
- Fix url path: INSERT LINK

## FLAW 2: Cross-Site Request Forgery (CSRF)

#### Exact source

- INSERT LINK

#### Description

#### How to fix it

review post doesn't include csrf token

## FLAW 3: Injection (Cross-Site Scripting (XSS))

#### Exact source

- INSERT LINK

#### Description

#### How to fix it

reviews.html

## FLAW 4: Cryptographic Failures

#### Exact source

- INSERT LINK

#### Description

#### How to fix it

secret key in git, debug is true, dev database is in git

## FLAW 5: Identification and Authentication Failures

#### Exact source

- INSERT LINK

#### Description

#### How to fix it

simple session
