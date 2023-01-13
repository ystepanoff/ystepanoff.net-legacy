export DJANGO_SECRET_KEY=`date | sha512sum | sed 's/\s.*$//'`
export DJANGO_DEBUG=False
