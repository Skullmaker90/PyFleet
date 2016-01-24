# PyFleet

PyFleet is a utility that is used to parse and monitor Chatlogs for the game Eve Online. Each module function is explained below,
I'm open to suggestions on how to improved this as I know there is better ways of doing things.

### Modules:
------------------------

###### dir_sort.py

Syntax: ``` a.newest("/folder/path/", "filename*") ``` Note the trailing "/" for the path, it's required. Also the filename takes regex. This will return the path of the most recently created file in a directory, used because of how EvE creates new logs every time the game is re/started.

###### log_parse.py

Syntax ``` a.log_parse("/Absolute/file/path.txt") ``` The real meat of the script is here, requires the file to be encoded in utf-16-le. Opens the file, then will do an initial parsing and from then on just append the log list with any further updates. Format is as such for each line: ```['timestamp', 'pilot name', 'message text']```. Each line is then appended together in a list. This will then chop the first 12 lines (13 if there is an MOTD) off the list and output it.

###### key_watch.py

Syntax: ``` a.key_watch(log_parse_list, "keyword") ``` This will take the array outputed from log_parse and a set "Keyword" (such as !fb) and compare it to the 'message text' of the last line. It will only compare against the first first element (broken up by whitespaces) e.g.: ``` 'This is my message' ``` The keyword will be compared against "This". Class will only return line if a key has been found. Will also output to console.

###### slack_post.py

Syntax: ``` a.slack_post(parsed_line) ``` This will take a log_parsed formatted line and post it to slack. I will be updating this to require a channel on calling in the future but for now it can be changed by editing the ``` self.payload['channel'] ```line. Requires and auth token from slack team.

run.py just instantiates everything together and creates a loop to watch for the key, updating the parsed_log every second. Currently because slack requires utf-8 for post requests some characters will return x00 when parsed.
