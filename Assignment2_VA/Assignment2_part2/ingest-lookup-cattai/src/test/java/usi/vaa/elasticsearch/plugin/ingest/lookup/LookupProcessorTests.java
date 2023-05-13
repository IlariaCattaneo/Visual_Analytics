/*
 * Copyright [2021] [Ilaria Cattaneo]
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */


package usi.vaa.elasticsearch.plugin.ingest.lookup;

import org.elasticsearch.ingest.IngestDocument;
import org.elasticsearch.ingest.Processor;
import org.elasticsearch.ingest.RandomDocumentPicks;
import org.elasticsearch.test.ESTestCase;
import org.junit.BeforeClass;
import java.util.HashMap;
import java.util.Map;

import static org.hamcrest.Matchers.equalTo;

public class LookupProcessorTests extends ESTestCase {


    @BeforeClass
    public static void defaultSettings() {
        System.setProperty("tests.security.manager", "false");
    }

    public void testSimple() throws Exception{
        LookupProcessor.Factory factory = new LookupProcessor.Factory();
        Map<String, Object> config = new HashMap<>();
        config.put("field", "field1");
        config.put("lookup-map", Map.of("C001", "tyre", "C010", "front wing", "C100", "damper"));
        Map<String, Processor.Factory> factories = Map.of(LookupProcessor.TYPE, factory);

        LookupProcessor processor = factory.create(factories, "lookup", "lookup", config);

        IngestDocument ingestDocument = RandomDocumentPicks.randomIngestDocument(random(), Map.of("field1", "Need to optimize the C001 temperature. C010 needs to be changed as it is damaged. C100 seems ok."));
        processor.execute(ingestDocument);

        assertThat(ingestDocument.getFieldValue("field1", String.class), equalTo("Need to optimize the tyre temperature. front wing needs to be changed as it is damaged. damper seems ok."));

    }

    public void testEmptyField() throws Exception{
        LookupProcessor.Factory factory = new LookupProcessor.Factory();
        Map<String, Object> config = new HashMap<>();
        config.put("field", "field1");
        config.put("lookup-map", Map.of("C001", "tyre", "C010", "front wing", "C100", "damper"));
        Map<String, Processor.Factory> factories = Map.of(LookupProcessor.TYPE, factory);

        LookupProcessor processor = factory.create(factories, "lookup", "lookup", config);

        IngestDocument ingestDocument = RandomDocumentPicks.randomIngestDocument(random(), Map.of("field1", ""));
        processor.execute(ingestDocument);

        assertThat(ingestDocument.getFieldValue("field1", String.class), equalTo(""));

    }

}
