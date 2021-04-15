test:
	 pipenv run pytest tests --cov=. --cov-report html:report -vvvv

run_main:
	pipenv run python main.py