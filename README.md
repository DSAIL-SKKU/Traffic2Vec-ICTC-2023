# Network Data Generation using IP2Vec Embedding

Network data generation is crucial in applying deep learning techniques for predicting and managing 5G/6G networks. In this paper, we propose to incorporate IP2Vec in generative adversarial networks (GAN)-based network data generation models. Our evaluation demonstrates that utilizing IP2Vec can effectively enhance the performance of GANs in generating network data.

This codebase contains the python scripts for the model for the ICTC 2023. (The paper has not yet been officially published.)

## Data

To learn the proposed model, we utilize an open source *[traffic prediction dataset](https://www.sciencedirect.com/science/article/pii/S1389128620312081).*

The dataset comprises network packets gathered between February 20th and October 6th in 2019. It encompasses various components such as packet timestamp, protocol, payload size, source/destination IP addresses, source/destination UDP/TCP ports, and user activity types (i.e., Interactive, Bulk, Video, and Web). The user activity types can be summarized as follows.

- *Interactive*: Interactive activity includes traffic from real time interactive applications such as chatting app or remote file editing in Google Docs.
- *Bulk*: Bulk data transfer activity consists of traffic to applications that use significant portions of the network’s bandwidth for large data file transfers, e.g., large file downloads from Dropbox.
- *Video*: Video playback activity includes traffic from applications consuming videos (e.g., from Twitch or YouTube).
- *Web*: Web browsing consists of traffic for all activities within a web page such as downloading images or ads.


## Run

### 1. IP2Vec
```python
python ip2Vec/train.py --data --dir

## Example
python ip2Vec/train.py bulk data/bulk_vec
```

—data: A factor that selects data for conversion into a vector format.


—dir: A factor that selects a directory in which data will be stored.


<br/>

```python
python ip2Vec/preprocess.py
python ip2Vec/embedding.py --data --dir

## Example
python ip2Vec/embedding.py data/bulk_vec data/bulk_emb
```

The file takes models trained from pre-training and conducts transfer learning on relatively small traffic volume data such as *bulk*, *video*, and *web*.

—data: A factor that selects data for conversion into a vector format.


—dir: A factor that selects a directory in which data will be stored.


<br/>


The left figure below defines the **IP2Vec** architecture in folder `ip2Vec/model.py`.

<br/>
<img width="450" alt="image" src="https://github.com/DSAIL-SKKU/IP2Vec-ICTC-2023/assets/60170358/eef5f203-230a-44fe-b605-2ca1965be223">

<br/>

### 2. GAN
In this paper, we trained and generated data using four widely-used GAN models. The descriptions of each model is summarized as follows.

- *GMMN*: GMMN is a model that effectively optimizes the Minimax loss by leveraging Maximum Mean Discrepancy (MMD). It is a variation of GANs, where MMD is used during the optimization process between the generator and discriminator to minimize the difference between distributions.
- *RCGAN*: RCGAN, which stands for Recurrent Conditional Generative Adversarial Network, is a specialized conditional generative model designed for sequence data generation. RCGAN focuses on generating time series data based on given conditions.
- *TimeGAN*: TimeGAN is a specialized model for time series data, which trains both autoencoding components and adversarial components together. It uses a Recurrent Neural Network (RNN)-based autoencoder to capture the characteristics of time series data, and generates realistic time series data through adversarial networks. TimeGAN can learn patterns and dependencies that change over time in the data.
- *SigCWGAN*: SigCWGAN is a model trained to capture the temporal dependence of conditional probabilities in time series data. It is a variation of Conditional Wasserstein GAN (CWGAN), where the optimization process between the generator and discriminator captures the temporal dependence of conditional probabilities derived from time series data.
<br/>

```python
python GAN/train_GAN.py --algos --datasets

## Example
python GAN/train_GAN.py bulk_emb
```

—datasets: A factor that selects data to train GAN.

—algos: A factor that selects the GAN model to be used for generation. Default value is all four models of GAN.

<br/><br/>

The right figure below defines the **GAN** architecture in folder `GAN`.
<br/>
<img width="450" alt="image" src="https://github.com/DSAIL-SKKU/IP2Vec-ICTC-2023/assets/60170358/eef5f203-230a-44fe-b605-2ca1965be223">


## Performance

<img width="441" alt="image" src="https://github.com/DSAIL-SKKU/IP2Vec-ICTC-2023/assets/60170358/47b81434-fd5f-44f7-8183-7d4db16a1003">


Both R2 comparison and discriminative score generally exhibited lower values when using IP2Vec compared to not using it in most cases. Particularly, the GMMN and SigCWGAN models demonstrated superior performance in terms of discriminative score when IP2Vec was applied for all data types. When examining the performance for each data type, web data showed the largest improvement in terms of R2 comparison compared to other data types. Specifically, when the GMMN model was trained on web data, it achieved a value of 0.76, but when IP2Vec was introduced, it showed a performance of 0.22, resulting in a remarkable performance difference of 0.54. This result indicates that even models like GMMN, which do not capture the characteristics of time series data well, can achieve more effective data generation by leveraging IP2Vec.
