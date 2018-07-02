# ChatEval
A scientific framework for evaluating chatbots. Scientific
paper available [here](https://github.com/chateval/ChatEval/blob/master/paper/Chatbot_Evaluation_Demo_2018_EMNLP.pdf).

## Dependencies
- Django (web framework)
- Bulma (CSS framework)
- MySQL (database)
- Amazon S3 (Dataset storage)
- Magnitude (word embedding format)

## Usage
0. Install dependencies using `pip install -r requirements.txt`.
2. Edit database information in `/chateval/settings.py`.
3. Run server migrations using `python manage.py makemigrations && python manage.py migrate`.
4. Create an `env.sh` (and source using `source env.sh`) containing:
```
export DB_NAME=
export DB_USER=
export DB_PASSWORD=
export DB_HOST=
export DB_PORT=
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_STORAGE_BUCKET_NAME=
```
5. Run server using `python manage.py runserver`
6. Download `.magnitude` word embeddings from [here](http://magnitude.plasticity.ai/word2vec/GoogleNews-vectors-negative300.magnitude) and place the vectors in `/eval/scripts/files/google_news.magnitude`.
7. Populate database using `python manage.py loaddata init.json`.
8. Access app at [localhost:8000](localhost:8000) and admin SQL page at [localhost:8000/admin](localhost:8000/admin).

## Code Documentation
Documentation for the codebase is available in `DOCUMENTATION.md`.
