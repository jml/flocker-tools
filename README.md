# flocker-tools

Experimental repository for prototypes of tools for administering and debugging
flocker clusters.

## Log analysis

Requires [eliot-tree](https://github.com/jonathanj/eliottree).

The following will find and display all actions taken by the dataset agent for
a particular `dataset_id` that contain a failed action.

```
$ journalctl --all --output=cat --unit="flocker-dataset-agent.service" > dataset.log
$ repair-json dataset.log > dataset-fixed.log 2> discarded-entries.log
$ eliot-tree --select 'action_status==`failed`' --select 'dataset_id==`$SOME_UUID`' dataset.log  | tee dataset-tree
```

## Log export

If you are using flocker 1.2 or later, then use the built-in
`flocker-diagnostics` tool.

If you are using earlier versions of flocker, try
[flocker-log-export.sh](flocker-log-export.sh). For example:

```
$ sudo ./flocker-log-export.sh
$ aws s3 cp clusterhq_flocker_logs* s3://some-bucket/some-folder/
```
