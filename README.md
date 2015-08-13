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
