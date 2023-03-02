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

### Exact source

- INSERT LINK

### Description

The review route gets user id as parameters when doing GET request to `review/<user id>`. However this route doesn't have login required, and it also allows everyone to see other user's received and given reviews, which should be hidden from others than participants of the review. Meaning by simply changing the user id anyone can see every review.

### How to fix it

This flaw can be fixed by first making the route require login to access. Then the route should be changed to just `review/`. After that the user should be fetched from request, and not from the url.

Links to fixes:
- Fix login required: INSERT LINK
- Fix user fetch: INSERT LINK
- Fix url path: INSERT LINK

## FLAW 2: Cross-Site Request Forgery (CSRF)

### Exact source

- INSERT LINK

### Description

The review add route isn't protected from Cross-Site Request Forgery (CSRF). As the name indicates, this allows attacker to make user do unintended actions on site they're logged in to when visiting the attacker's own site. In this case it means that the attacker could make the user send inappropriate reviews to others.

### How to fix it

This flaw can be fixed by first making the route require CSRF token. Then we'll have to add the CSRF token to the form that is used to add the review. With Django the fix is fairly easy, as I had to intentionally make the route vulnerable by adding `@csrf_exempt`. In other frameworks this isn't always this easy.

Links to fixes:
- Fix CSRF requirement: INSERT LINK
- Fix CSRF form: INSERT LINK

## FLAW 3: Injection (Cross-Site Scripting (XSS))

### Exact source

- INSERT LINK

### Description

The added reviews can contain HTML and/or JavaScript. This results into that attacker can run scripts in the user's machine when they visit their reviews site, which doesn't have protection against XSS. Attacker is then able to run anything as that user, which means for example that attacker can send all of the user's information to their own databases.

### How to fix it

This flaw can be fixed by adding validation to reviews so that they're not interpreted as HTML and/or JavaScript. With Django this is also easy to fix, as I had to make this vulnerability intentionally into the code. Only thing we'll have to do is remove `|safe` and Django will handle the rest. It is good to remember here also that other frameworks might not have it this easy. 

Links to fixes:
- Fix XSS for received: INSERT LINK
- Fix XSS for given: INSERT LINK

## FLAW 4: Cryptographic Failures

### Exact source

- INSERT LINK

### Description

Under cryptographic failures also falls sensitive data exposures. Currently the project has `SECRET_KEY` hardcoded into `settings.py`, which allows the attacker to directly see what master key is used. Project also has `DEBUG=True`, and if this build would reach the production the attacker could easily gain information of things such as: source code, settings and libraries used. Database used in development is also exposed publicly in Github which can contain sensitive information which may find its way to production.

### How to fix it

These flaws are fairly easy to fix. We'll need to add `.env` file with `SECRET_KEY` and `IS_DEV`. This way secret isn't exposed to public, and debug is disabled when in production. It is good to remember that `.gitignore` has to exclude `.env` files. Database has to be added to `.gitignore`, and then it should be removed from git history to prevent any kind of access to it.

Links to fixes:
- Fix secret key and debug: INSERT LINK

## FLAW 5: Identification and Authentication Failures

### Exact source

- INSERT LINK

### Description

### How to fix it

simple session
