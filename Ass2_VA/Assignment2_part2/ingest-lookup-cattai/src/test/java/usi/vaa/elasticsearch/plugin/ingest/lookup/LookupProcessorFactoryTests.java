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

import org.elasticsearch.ElasticsearchParseException;
import org.elasticsearch.ingest.Processor;
import org.elasticsearch.test.ESTestCase;
import org.junit.BeforeClass;

import java.util.HashMap;
import java.util.Map;

import static org.hamcrest.Matchers.equalTo;

public class LookupProcessorFactoryTests extends ESTestCase {

    @BeforeClass
    public static void defaultSettings() {
        System.setProperty("tests.security.manager", "false");
    }

    private Map<String, Object> getDefaultConfig() {
        Map<String, Object> config = new HashMap<>(Map.of());
        config.put("field", "field1");
        config.put("lookup-map", Map.of());
        return config;
    }

    public void testDefaultConfiguration() throws Exception{
        LookupProcessor.Factory factory = new LookupProcessor.Factory();
        Map<String, Object> config = getDefaultConfig();
        Map<String, Processor.Factory> factories = Map.of(LookupProcessor.TYPE, factory);

        LookupProcessor processor = factory.create(factories, "lookup", "lookup", config);

        assertThat(processor.getField(), equalTo("field1"));
        assertThat(processor.getLookupMap(), equalTo(Map.of()));
    }

    public void testInvalidConfiguration() throws Exception{
        LookupProcessor.Factory factory = new LookupProcessor.Factory();
        Map<String, Object> config = getDefaultConfig();
        config.put("field", null);
        Map<String, Processor.Factory> factories = Map.of(LookupProcessor.TYPE, factory);

        ElasticsearchParseException e = expectThrows(ElasticsearchParseException.class,
                () -> factory.create(factories, "lookup", "lookup", config));
        assertThat(e.getMessage(), equalTo("[field] required property is missing"));
    }

}
