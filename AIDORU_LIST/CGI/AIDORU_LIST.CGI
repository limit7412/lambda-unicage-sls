#!/bin/sh
# MODEによって処理を振り分ける

# tukubaiコマンドへのPATH
export PATH=$PATH:$LAMBDA_TASK_ROOT/bin/
# aws cliへのPATH
export PATH=$PATH:/opt/awscli
app_name="AIDORU_LIST"
basename="$(basename $0)"
tmp="/tmp/${basename}-$$"
app_dir="$LAMBDA_TASK_ROOT/${app_name}"

case "${MODE}" in
  init )
    ${app_dir}/CGI/${app_name}.DISPLAY
    ;;
  toroku )
    # 入ってきたeventをユニケージ用にパース
    ${app_dir}/CGI/event2name.py ${1} > ${tmp}-event
    ${app_dir}/CGI/${app_name}.TOROKU ${tmp}-event
    ;;
esac
