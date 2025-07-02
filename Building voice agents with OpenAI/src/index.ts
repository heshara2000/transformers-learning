import { Agent } from '@Openai/agents';
import z from 'zod';

const getWeather = tool({
    name: "getWeather",
    description: "Get the current weather for a given location.",
    parameters: z.object({
        location: z.string(),
    }),
    execute: async ({location}) => {
        return `the weather in ${location} is sunny`;
    },
});

const agent = new Agent({
    name: "My Agent",
    instructions: "You are a helpful assistant.",
    model: "04-mini",
    tools: [getWeather],
})

const result = await run(agent, "hello how are you?");

console.log(result.finalOutput);