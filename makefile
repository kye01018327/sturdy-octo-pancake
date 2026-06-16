make:
	python ./scripts/plot_commute_home.py
	python ./scripts/plot_commute_work.py

all:
	python ./scripts/get_commute_work.py
	python ./scripts/get_commute_home.py

	python ./scripts/plot_commute_home.py
	python ./scripts/plot_commute_work.py