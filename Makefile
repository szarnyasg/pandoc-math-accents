compile:
	pandoc test.md --output=test.pdf --from=markdown --variable=lang:magyar --filter ./mathaccents.py
