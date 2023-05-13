# Elasticsearch Lookup Ingest Processor (stub)

Here is a partially complete repo that you should use to create a lookup ingest processor plugin for ElasticSearch. Given a field and a lookup-map, the processor, when ingesting a document, will apply the given lookup-map on the given field, thus replacing all occurrences of the map keys, with the map values. The idea is to, for example, replace product codes with product names, or replace id-emails with the corresponding name-email.

For example, if my documents are about a car and I know that code C001 means tyre, when ingesting a document I want to replace all occurrences of C001 with tyre, so that a document with field = "Need to optimize the C001 temperature", would be indexed as "Need to optimize the tyre temperature".


## Expected results


Once installed, your plugin should work as follows.

First you register a pipeline, using your processor plugin (processors => lookup)


```
PUT _ingest/pipeline/lookup-pipeline
{
  "description": "A lookup pipeline",
  "processors": [
    {
      "lookup" : {
      "field" : "field1",
      "lookup-map" : {
        "C001":"tyre" ,
        "C010":"front wing",
        "C100":"damper"
      }
    }
  }]
}
```

Then you ingest a document on an index using the pipeline you just registered

```
PUT something/_doc/1?pipeline=lookup-pipeline
{
  "field1" : "Need to optimize the C001 temperature. C010 needs to be changed as it is damaged. C100 seems ok."
}
```

When ingesting the document, ElasticSearch will apply your processor, thus replacing the lookup-map keys with values. When you get the document you just ingested, you should get the following:

```
GET something/_doc/1
{
  ...
  "_source" : {
    "field1" : "Need to optimize the tyre temperature. front wing needs to be changed as it is damaged. damper seems ok."
  }
}
```


## How to

To open the project with Idea, you should run

```
./gradlew idea
open ingest-lookup.ipr
```

To install the plugin, you need to perform the following operation.

```bash
./gradlew build
```

This will build the plugin, also running all tests, checkstyle and findbugs. If tests are not green or if there are checkstyle / findbugs violation, the project will not build, so you need to fix your code in order to build the plugin.

Once the gradle build successfully completes, you will find a zip file named `ingest-lookup-8.6.2.zip` in `build/distributions`. You can install the plugin in ElasticSearch with the following command:

```
<ES-LOCATION>/bin/elasticsearch-plugin install --batch file:/<PATH-TO-LOOKUP-PLUGIN>/build/distributions/ingest-lookup-8.6.2.zip
```

If you want to build your plugin, without running all the tests, you can use the following command:

```bash
./gradlew assemble
```
