Add comment to JIRA

Usage:
  jira-comment --bug-id=BUG_ID [options] ([-] | --comment_file=<comment_file>)
  jira-comment (-h | --help)
  jira-comment (-v | --version)

Options:
  -f --comment-file=<comment_file>  File with comment text [default: /dev/stdin]
  -s --server=<server>              Server URI for Jira [default: JIRA_SERVER] (environment variable)
  -u --username=<username>          Username for Jira [default: JIRA_USERNAME] (environment variable)
  -p --password=<password>          Password for Jira [default: JIRA_PASSWORD] (environment variable)
  -d --debug                        Enable debug output
  -h --help                         Show this screen.
  -v --version                      Show version.

Examples:
  echo "my comment" | jira-comment --bug-id=JIRA-271
  jira-comment --bug-id=JIRA-271 --comment-file=comment.txt