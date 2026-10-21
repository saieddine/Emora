# Emora — Local AI Companion

## Project Vision
Emora is a research-oriented project exploring a friendly, privacy-preserving AI companion that can understand conversational context, recognize possible emotional cues, and maintain user-approved memories.

## Long-Term Goals
- Run AI models locally.
- Explore emotion-aware conversational responses.
- Develop privacy-conscious conversational memory.
- Build a voice interface and animated avatar.
- Evaluate the system through reproducible experiments.
- Investigate potential applications in human-computer interaction and robotics.

## Research Principle
Emora will treat emotion recognition as uncertain inference rather than claiming to know a person's internal feelings.
# Emora — A Local, Emotion-Aware AI Companion

**Emora** is a long-term AI engineering and research project focused on building a personal AI companion that can communicate naturally, understand conversational context, recognize emotional cues, and gradually develop useful long-term memory — while keeping user data and AI inference local whenever possible.

The project begins as a local software assistant and may eventually explore multimodal interaction and embodied AI.

> **Project status:** Early development and learning phase. Features described in the roadmap are planned unless explicitly marked as implemented.

## Vision

The goal of Emora is to explore how locally running AI systems can become more personalized, context-aware, and natural to interact with.

Rather than relying entirely on remote AI services, Emora aims to use open-source tools and locally runnable models to build a system that prioritizes privacy, transparency, and user control.

## Planned Features

- **Local AI inference:** Run compatible open-weight language models locally.
- **Natural conversation:** Answer questions and maintain conversational context.
- **Emotion-aware interaction:** Explore emotional cues in language and adapt responses cautiously.
- **Voice interaction:** Support speech input and locally generated speech output.
- **Animated interface:** Create a visual character that responds during conversations.
- **Personal memory:** Store useful information with user consent and provide control over what is remembered.
- **Local knowledge retrieval:** Retrieve relevant information from selected documents to improve answers.
- **Future multimodal capabilities:** Explore combining text, speech, and other inputs.
- **Future embodied AI research:** Investigate how conversational AI could connect to a physical robot with appropriate safety controls.

## Design Principles

1. **Privacy first:** Prefer local processing and avoid sending personal data to external services unnecessarily.
2. **User control:** Make stored memories inspectable, editable, and deletable.
3. **Honest emotional understanding:** Treat emotion recognition as uncertain inference, not as direct access to a person's feelings.
4. **Modular architecture:** Keep components independent so that models and tools can be replaced as the project evolves.
5. **Evidence-driven development:** Evaluate features with experiments, measurable metrics, and documented limitations.
6. **Safety by design:** Avoid presenting Emora as a therapist or a substitute for professional support.

## Planned Architecture

The initial architecture is expected to follow this flow:

```text
User
 |
 v
Input Interface
 |-- Text
 |-- Microphone (planned)
 |
 v
Input Processing
 |-- Speech Recognition (planned)
 |-- Text Processing
 |
 v
Conversation Engine
 |-- Local Language Model
 |-- Conversation Context
 |-- Emotion Cue Analysis
 |-- Knowledge Retrieval
 |-- User-Controlled Memory
 |
 v
Response Generation
 |-- Local Text-to-Speech (planned)
 |-- Text Response
 |
 v
User Interface
 |-- Chat
 |-- Animated Avatar (planned)
```

The architecture is provisional and will evolve as individual components are implemented and tested.

## Technology Direction

The following technologies are candidates for the project, not a claim that every component is already integrated.

| Area | Candidate technologies |
|---|---|
| Programming language | Python |
| Development environment | Visual Studio Code |
| Machine learning | PyTorch, scikit-learn |
| Model integration | Hugging Face Transformers |
| Local model inference | Ollama or llama.cpp |
| Data and memory | SQLite |
| Information retrieval | Embeddings and local vector search |
| Speech recognition | Whisper or faster-whisper |
| Speech generation | Piper or another locally runnable TTS system |
| Frontend | HTML, CSS, JavaScript |
| Version control | Git and GitHub |
| Future robotics | ROS 2 |

Technology choices will depend on hardware compatibility, latency, model quality, and privacy requirements.

## Development Roadmap

### Phase 1 — Foundations
- Build a reliable Python development environment.
- Learn the mathematics behind machine learning.
- Practice NumPy, probability, statistics, and basic neural networks.
- Establish version control and project documentation.

### Phase 2 — Machine Learning
- Learn PyTorch and automatic differentiation.
- Train and evaluate a simple text classifier.
- Explore emotion-related text datasets.
- Analyze errors, limitations, and evaluation metrics.

### Phase 3 — Local Language Models
- Study tokenization and Transformer architecture.
- Run a small compatible language model locally.
- Build a command-line conversational prototype.
- Experiment with local document retrieval and grounded answers.

### Phase 4 — Voice and Interface
- Integrate local speech recognition.
- Add text-to-speech.
- Build an interactive interface with an animated avatar.
- Measure end-to-end response latency.

### Phase 5 — Memory and Research
- Design a user-controlled local memory system.
- Compare responses with and without memory.
- Study related research on affective computing and personalized AI.
- Evaluate privacy, usefulness, reliability, and emotional inference errors.

### Phase 6 — Integration and Future Exploration
- Combine the working components into a coherent prototype.
- Test realistic conversations and failure cases.
- Document experimental results.
- Explore multimodal interaction and robotics as future research directions.

## Hardware and Privacy

Emora is intended to favor local inference, but model selection will depend on available memory, compute resources, and acceptable response speed.

Development will begin with lightweight experiments. Larger models or training experiments may require access to more powerful hardware.

The project aims to keep conversation data and personal memories local by default. Any future external service integration should be explicit and documented.

## Research Questions

Potential research directions include:

- Can a lightweight emotion classifier improve conversational responses without excessive false positives?
- Does user-controlled long-term memory improve answer relevance and consistency?
- What trade-offs exist between model size, response quality, privacy, and latency in local AI companions?
- How can a system communicate uncertainty when interpreting emotional cues?

These are exploratory questions, not established results.

## Current Status

Emora is in its early development stage. Work is focused on building the mathematical, programming, and machine-learning foundations needed for a reliable prototype.

Implemented features and experimental results will be documented here as they become available.

## Contributing and Development

The project is currently developed as a learning and research project. The codebase and architecture may change as experiments reveal better approaches.

Before contributing, check the current project structure and setup instructions. Installation steps will be added once the initial application dependencies and runtime are established.

## License

A license has not yet been selected. Until one is added, reuse and redistribution permissions should not be assumed.

---

**Emora — exploring private, personalized, emotion-aware AI, one experiment at a time.**
