# Tietoturvan perusteet: Project I

LINK: https://github.com/Perttu-Kangas/csb-project

This project uses OWASP 2021 list.

Make sure you have Python and Django installed.

## Installation

1. Clone repo
2. Go to cloned repo folder in terminal
3. Start the app by `python3 manage.py runserver`
4. Log in using username `alice` and password `redqueen`

Or with Docker

1. docker build -t csb-project .
2. docker run -p 8000:8000 csb-project

## FLAW 1: Broken Access Control

https://github.com/Perttu-Kangas/csb-project/blob/main/pages/views.py#L23

### Description

The review route gets user id as parameters when doing GET request to `review/<user id>`. However this route doesn't have login required, and it also allows everyone to see other user's received and given reviews, which should be hidden from others than participants of the review. Meaning by simply changing the user id anyone can see every review.

### How to fix it

This flaw can be fixed by first making the route require login to access. Then the route should be changed to just `review/`. After that the user should be fetched from request, and not from the url.

Links to fixes:

- Fix login required: [views.py#L21](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/views.py#L21)
- Fix user fetch: [views.py#L26](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/views.py#L26)
- Fix url path: [urls.py#L9](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/urls.py#L9)

## FLAW 2: Cross-Site Request Forgery (CSRF)

https://github.com/Perttu-Kangas/csb-project/blob/main/pages/views.py#L11

### Description

The review add route isn't protected from Cross-Site Request Forgery (CSRF). As the name indicates, this allows attacker to make user do unintended actions on site they're logged in to when visiting the attacker's own site. In this case it means that the attacker could make the user send inappropriate reviews to others.

### How to fix it

This flaw can be fixed by first making the route require CSRF token. Then we'll have to add the CSRF token to the form that is used to add the review. With Django the fix is fairly easy, as I had to intentionally make the route vulnerable by adding `@csrf_exempt`. In other frameworks this isn't always this easy.

Links to fixes:

- Fix CSRF requirement: [views.py#L8](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/views.py#L8)
- Fix CSRF form: [index.html#L29](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/templates/pages/index.html#L29)

## FLAW 3: Injection (Cross-Site Scripting (XSS))

https://github.com/Perttu-Kangas/csb-project/blob/main/pages/templates/pages/reviews.html#L10

### Description

The added reviews can contain HTML and/or JavaScript. This results into that attacker can run scripts in the user's machine when they visit their reviews site, which doesn't have protection against XSS. Attacker is then able to run anything as that user, which means for example that attacker can send all of the user's information to their own databases.

### How to fix it

This flaw can be fixed by adding validation to reviews so that they're not interpreted as HTML and/or JavaScript. With Django this is also easy to fix, as I had to make this vulnerability intentionally into the code. Only thing we'll have to do is remove `|safe` and Django will handle the rest. It is good to remember here also that other frameworks might not have it this easy.

Links to fixes:

- Fix XSS for received: [reviews.html#L8](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/templates/pages/reviews.html#L8)
- Fix XSS for given: [reviews.html#L20](https://github.com/Perttu-Kangas/csb-project/blob/main/pages/templates/pages/reviews.html#L20)

## FLAW 4: Cryptographic Failures

https://github.com/Perttu-Kangas/csb-project/blob/main/config/settings.py#L25

### Description

Under cryptographic failures also falls sensitive data exposures. Currently the project has `SECRET_KEY` hardcoded into `settings.py`, which allows the attacker to directly see what master key is used. Project also has `DEBUG=True`, and if this build would reach the production the attacker could easily gain information of things such as: source code, settings and libraries used. Database used in development is also exposed publicly in Github which can contain sensitive information which may find its way to production.

### How to fix it

These flaws are fairly easy to fix. We'll need to add `.env` file with `SECRET_KEY` and `IS_DEV`. This way secret isn't exposed to public, and debug is disabled when in production. It is good to remember that `.gitignore` has to exclude `.env` files. Database has to be added to `.gitignore`, and then it should be removed from git history to prevent any kind of access to it.

Links to fixes:

- Fix secret key and debug: [settings.py#L22](https://github.com/Perttu-Kangas/csb-project/blob/main/config/settings.py#L22)

## FLAW 5: Identification and Authentication Failures

https://github.com/Perttu-Kangas/csb-project/blob/main/config/settings.py#L94

### Description

When user logs in session id is generated for them. Currently project has really weak session id generator. Session id are currently in form of `<int>-verysekretsession-<int>` which means attacker can easily crack current sessions. Using these cracked sessions attacker can do anything they want as that user. In this case it would be mean that they could read user's reviews and send inappropriate reviews to others.

### How to fix it

This flaw is also really easy to fix as Django handles this automatically and I had to intentionally cause this. We'll have to change `SESSION_ENGINE` to engine that does better cryptographic signing. In Django this means that we'll let the `SESSION_ENGINE` use the default one by removing it from `settings.py`. Django uses `SECRET_KEY` to sign the session id. As mentioned `SECRET_KEY` is used here which is why flaw 4 is also really important to fix.

Links to fixes:

- Fix secret engine: [settings.py#L92](https://github.com/Perttu-Kangas/csb-project/blob/main/config/settings.py#L92)
- Delete simplesession.py: [simplesession.py](https://github.com/Perttu-Kangas/csb-project/blob/main/config/simplesession.py)
