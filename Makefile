dev:
	bundle exec jekyll serve --drafts

install:
	bundle install --path ~/.gem
	bundle add webrick
