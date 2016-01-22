DIR="$( cd "$( dirname "${BASH_SOURCE[1]}" )" && pwd)"
spark-submit main.py --path $1 --op vb