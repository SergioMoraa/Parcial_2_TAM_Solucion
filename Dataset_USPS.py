{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbawkUnESBogA1g8OfQnUd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SergioMoraa/Parcial_2_TAM_Solucion/blob/main/Dataset_USPS.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aFoqTpHuPVrM",
        "outputId": "1533232d-108c-4f98-d763-77a40a07af41"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading from https://www.kaggle.com/api/v1/datasets/download/bistaumanga/usps-dataset?dataset_version_number=1...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 2.75M/2.75M [00:00<00:00, 114MB/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Extracting files...\n",
            "Path to dataset files: /root/.cache/kagglehub/datasets/bistaumanga/usps-dataset/versions/1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        }
      ],
      "source": [
        "import kagglehub\n",
        "\n",
        "# Download latest version\n",
        "path = kagglehub.dataset_download(\"bistaumanga/usps-dataset\")\n",
        "\n",
        "print(\"Path to dataset files:\", path)"
      ]
    }
  ]
}