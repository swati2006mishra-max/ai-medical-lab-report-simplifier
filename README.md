# AI Medical Lab Report Simplifier

AI-powered medical lab report simplifier using OCR and AI to extract and simplify medical test results.

## Features

- 📄 **OCR Processing**: Extracts text from medical lab report images using Tesseract OCR
- 🤖 **AI-Powered Simplification**: Uses OpenAI's GPT models to simplify complex medical terminology
- 📊 **Structured Output**: Converts raw lab data into easy-to-understand formats
- 🔐 **Privacy-Focused**: Process reports locally with optional API integration
- ⚡ **Fast & Efficient**: Batch processing support for multiple reports

## Installation

### From GitHub (Direct Installation)

```bash
pip install git+https://github.com/swati2006mishra-max/ai-medical-lab-report-simplifier.git
```

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/swati2006mishra-max/ai-medical-lab-report-simplifier.git
cd ai-medical-lab-report-simplifier
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.8 or higher
- Tesseract OCR (for image text extraction)
- OpenAI API key (for AI-powered simplification)

### Install Tesseract OCR

**On macOS:**
```bash
brew install tesseract
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**On Windows:**
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
TESSERACT_PATH=/path/to/tesseract  # Optional, if not in PATH
```

## Usage

```python
from ai_medical_lab_report_simplifier import SimplifyReport

# Initialize
simplifier = SimplifyReport()

# Process a report image
result = simplifier.process_report("path/to/lab_report.pdf")

# Get simplified output
print(result.simplified_text)
print(result.key_findings)
```

## Project Structure

```
.
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .gitignore
└── src/
    ├── ocr/              # OCR processing modules
    ├── ai/               # AI simplification logic
    └── utils/            # Helper utilities
```

## Dependencies

- **opencv-python**: Image processing
- **pytesseract**: OCR wrapper for Tesseract
- **Pillow**: Image manipulation
- **openai**: GPT API integration
- **python-dotenv**: Environment variable management
- **requests**: HTTP requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub: [Issues](https://github.com/swati2006mishra-max/ai-medical-lab-report-simplifier/issues)

## Disclaimer

⚠️ **Important**: This tool is for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with a qualified healthcare provider for medical concerns.

---

**Built with ❤️ for healthcare accessibility**
