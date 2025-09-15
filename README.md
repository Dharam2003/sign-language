# Sign Language Translation

A real-time Sign Language detection and recognition system built using Python, OpenCV, and MediaPipe. The goal of this project is to detect hand signs and gestures from a live video feed and translate them to text.

-----

## Project Overview

This project aims to create a real-time sign language detection system that works with a webcam or live video input. It leverages **MediaPipe** for accurate hand landmark detection and **OpenCV** for video processing. A machine learning classifier is then trained on this data to recognize and classify hand signs.

**Key objectives of this project are:**

  * **Data Capture:** Create a dataset of hand sign images and landmarks.
  * **Model Training:** Develop a classifier to accurately recognize and categorize various hand signs.
  * **Real-time Inference:** Use the trained model to detect gestures in a live video stream.
  * **Application Packaging:** Build an application for real-time usage, with a potential UI or web interface for a better user experience.

-----

## Features

Based on the current codebase, the following features are fully or partially implemented:

  * **Data Collection:** Scripts like `collect_imgs.py` and `create_dataset.py` are used to gather and preprocess image data for a variety of signs.
  * **Model Training:** The `train_classifier.py` script handles the training of a classification model using the processed dataset.
  * **Real-time Detection:** The `inference_classifier.py`, `app.py`, and `run.py` scripts are designed to load a trained model and perform live predictions.
  * **Persistence:** The trained model is saved as `model.p`, and processed data is pickled into `data.pickle` for faster loading and re-use.
  * **Dependency Management:** All necessary Python packages are listed in `requirements.txt`.

-----

## Repository Structure

Here is a breakdown of the key files and folders within the repository:

| File / Folder | Purpose |
| :--- | :--- |
| `collect_imgs.py` | Script for capturing images and frames to build the sign language dataset. |
| `create_dataset.py` | Processes the collected images into a usable dataset for model training. |
| `train_classifier.py` | Trains the classification model using the prepared dataset. |
| `inference_classifier.py` | Loads the trained model to perform predictions on new inputs. |
| `app.py`, `run.py` | Serves as the entry point for real-time usage and application deployment. |
| `data/` | Contains images or raw data for different signs. |
| `data.pickle`, `model.p` | Stores the serialized data and the trained model for quick access. |

-----

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

  * **Python** (version 3.7 or newer recommended)
  * **Webcam** (essential for real-time detection)
  * **Sufficient storage** for your dataset and model files.

### Installation

To get started, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Dharam2003/sign-language.git
    cd sign-language
    ```

2.  **Install required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Verify your webcam access** through OpenCV using a simple test script.

### Running the App

Follow this workflow to run the sign language detection system:

1.  **Collect data** for your desired signs using `collect_imgs.py`.
2.  **Assemble and preprocess** the dataset with `create_dataset.py`.
3.  **Train the model** by running `train_classifier.py`.
4.  **Launch live detection** using either `inference_classifier.py` or `app.py`.

-----

## Model & Data

  * The trained model is a pickled classifier saved as **`model.p`**.
  * The preprocessed data is serialized and stored in **`data.pickle`** for efficient loading.
  * Sign labels and classes must be consistent across data collection, training, and inference.
  * Preprocessing is vital and includes resizing images, extracting landmarks using MediaPipe, and normalization.

-----

## Current Status

The project contains all the major building blocks—data collection, dataset creation, model training, and inference—and a working prototype is in place. The existence of `app.py` and `run.py` indicates a readiness for real-time application.

However, a few things are still in the early stages:

  * **User Interface:** There is currently no polished GUI. The user experience is primarily based on the command line and a live webcam feed.
  * **Documentation:** Usage examples and detailed instructions are minimal.
  * **Gesture Type:** The current system likely supports only static gestures. Handling dynamic or sequential gestures (e.g., letters like 'J' or 'Z' in ASL) may not be supported yet.
  * **Evaluation:** No formal evaluation metrics (like accuracy or confusion matrices) are published in the repository.
  * **Dataset Limitations:** The dataset is likely limited in size and diversity, which could affect the model's ability to generalize to new users, lighting conditions, or backgrounds.

-----

## Limitations

  * **Dataset Size & Diversity:** The model may perform poorly on new users or environments due to a limited and non-diverse dataset.
  * **Dynamic Gestures:** The system may struggle to interpret gestures that involve movement over time.
  * **Real-world Robustness:** Performance may degrade in the face of variations in lighting, camera angles, or hand occlusions.
  * **User Interface:** The lack of a front-end makes the user experience basic.
  * **Performance:** Depending on the hardware and model complexity, there may be some latency during real-time inference.
  * **Evaluation:** The absence of clear metrics makes it difficult to gauge the model's quality.

-----

## Future Updates

To enhance this project, here are some suggested improvements:

### Expand Dataset & Augment Data

  * Collect more data from a wider variety of users, lighting conditions, and backgrounds.
  * Use data augmentation techniques (e.g., rotations, scaling, brightness adjustments) to improve generalization.

### Support Dynamic Gestures

  * Integrate temporal modeling methods (e.g., LSTM, GRU, or transformer-based models) to handle gestures that change over time.

### Improve Real-time Inference & Deployment

  * Optimize the model for size and speed (e.g., through quantization or pruning).
  * Explore packaging the system into a lightweight web or mobile application.

### Enhance the User Interface (UI/UX)

  * Build a user-friendly GUI or web interface.
  * Display confidence scores and probabilities for predictions.

### Improve Robustness

  * Add features to handle noise, partial hand occlusions, and multiple hands.
  * Normalize performance across different skin tones and backgrounds.

### Add Evaluation & Benchmarking

  * Incorporate code to compute and report key metrics like accuracy, precision, and recall on a test set.

### Text-to-Speech Output

  * Add an optional feature to convert predicted signs into spoken output.

### Documentation & Examples

  * Write a more comprehensive README with detailed usage instructions and examples.
  * Provide clear steps for adding new gesture classes.

### Modularization & Code Clean-Up

  * Refactor the codebase for better modularity (e.g., separating data processing, modeling, and inference).
  * Implement better error handling and logging.

-----

## Contributing

We welcome contributions from everyone\! To contribute to this project:

1.  **Fork the repository** and create a new branch for your feature or bug fix.
2.  **Maintain a consistent coding style** throughout your changes.
3.  **Add comments and docstrings**, especially in core scripts.
4.  **If adding new gestures,** include sample data and update the data collection scripts.
5.  **Consider adding tests** (unit tests for core functions) to ensure code quality.