#!/bin/sh

# pm-utils hook to interact with Caffeine

STATUSFILE="/var/run/caffeine/status"

if [ -r "${PM_FUNCTIONS}" ]; then
	. "${PM_FUNCTIONS}" 
elif [ -r "${FUNCTIONS}" ]; then
	. "${FUNCTIONS}"
else
	# pm-utils version is too old, or something else is wrong
	exit $NA
fi

case "$1" in
	hibernate|suspend)
		# stop it
		status=$(cat $STATUSFILE)
		if [[ $status == '0' ]]; then
			inhibit "$1 inhibited by Caffeine"
		fi
		;;
	thaw|resume)
		# We aren't going to interfere with resuming
		;;
	*) exit $NA
		;;
esac
