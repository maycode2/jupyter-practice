Part 1: Theoretical Understanding
Q1: Explain the primary differences between TensorFlow and PyTorch. When would you choose one over the other?
TensorFlow and PyTorch are both open-source deep learning frameworks, but they have key differences:

Syntax and Ease of Use: PyTorch offers a more "Pythonic" interface, making it easier for beginners and more intuitive for dynamic computation. TensorFlow originally had a steeper learning curve but has improved significantly in version 2.x.

Execution Model: PyTorch uses eager execution by default (operations run immediately), which simplifies debugging. TensorFlow initially used static computation graphs but now supports eager execution as well.

Deployment: TensorFlow has better support for production deployment through tools like TensorFlow Serving, TensorFlow Lite (for mobile), and TensorFlow.js (for web). PyTorch supports deployment through TorchScript and ONNX but is often more research-focused.

Community and Ecosystem: TensorFlow has a more mature ecosystem with tools like TensorBoard, TFX, and Model Optimization Toolkit. PyTorch is favored in academia and research.

When to choose:

Choose PyTorch for rapid prototyping, academic work, and when ease of debugging is a priority.

Choose TensorFlow for robust production deployment, mobile/web apps, and when utilizing TensorFlow's larger ecosystem.

Q2: Describe two use cases for Jupyter Notebooks in AI development.
Interactive Experimentation and Visualization: Jupyter Notebooks allow developers to write and run code in chunks (cells), making it easier to test, visualize, and iterate on machine learning models. Visualization tools like Matplotlib or Seaborn integrate seamlessly.

Documentation and Tutorials: Jupyter Notebooks are widely used for sharing code along with explanations, making them ideal for educational purposes, team collaboration, and creating tutorials or reports.

Q3: How does spaCy enhance NLP tasks compared to basic Python string operations?
spaCy is a powerful NLP library that provides pre-trained pipelines and robust tools for language processing. Unlike basic string operations (e.g., split, lower, replace), spaCy can:

Recognize named entities (NER), parts of speech (POS), and syntactic dependencies.

Handle tokenization in a language-aware way.

Use word vectors and statistical models for advanced understanding of text.

This leads to more accurate, context-aware, and scalable NLP pipelines suitable for real-world applications.

