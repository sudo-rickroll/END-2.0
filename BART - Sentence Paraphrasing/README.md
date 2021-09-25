# Sentence Paraphrasing using BART

BART is an encoder-decoder model that is a combination of BERT and GPT. BERT is used as the encoder and GPT is used as the decoder. Since BERT can build the context of the sentences with a naturally high degree of accuracy and GPT can help in using the context to predict/generate the next sequence of texts, this model can also be used in the seq2seq architectures.

Here, we paraphrase sentences on Google data using Facebook's bart-base model.

Below are the sample predictions and training logs.

## Sample Predictions

```
Enter text to paraphrase: A recording of folk songs done for the Columbia society in 1942 was largely arranged by Pjetër Dungu.
Generating outputs:   0%|          | 0/1 [00:00<?, ?it/s]
---------------------------------------------------------
A recording of folk songs done for the Columbia society in 1942 was largely arranged by Pjetër Dungu.

Predictions >>>
A 1942 recording of folk songs done for Columbia society was largely arranged by Pjetër Dungu.
A 1942 recording of folk songs done for the Columbia society was largely arranged by Pjetër Dungu.
A recording of folk songs done for Columbia society in 1942 was largely arranged by Pjetër Dungu.
---------------------------------------------------------
```

```
Enter text to paraphrase: In mathematical astronomy, his fame is due to the introduction of the astronomical globe, and his early contributions to understanding the movement of the planets.
Generating outputs:   0%|          | 0/1 [00:00<?, ?it/s]
---------------------------------------------------------
In mathematical astronomy, his fame is due to the introduction of the astronomical globe, and his early contributions to understanding the movement of the planets.

Predictions >>>
In mathematical astronomy, his fame is due to the introduction of the astronomical globe and his early contributions to understanding the movement of the planets.
In mathematical astronomy, his fame is due to the introduction of the astronomical globe and his early contributions to understanding the movement of the planets.
In mathematical astronomy, his fame is due to the introduction of the astronomical globe and his early contributions to understanding the movement of the planets.
```

```
Enter text to paraphrase: Why are people obsessed with Cara Delevingne?
Generating outputs:   0%|          | 0/1 [00:00<?, ?it/s]
---------------------------------------------------------
Why are people obsessed with Cara Delevingne?

Predictions >>>
Why are people obsessed with Cara Delevingne?
Why are people obsessed with Cara Delevingne?
Why are people obsessed with Cara Delevingne?
---------------------------------------------------------
```

```
Enter text to paraphrase: Earl St Vincent was a British ship that was captured in 1803 and became a French trade man.
Generating outputs:   0%|          | 0/1 [00:00<?, ?it/s]
---------------------------------------------------------
Earl St Vincent was a British ship that was captured in 1803 and became a French trade man.

Predictions >>>
Earl St Vincent was a British ship captured in 1803 and became a French trade man.
Earl St Vincent was a British ship captured in 1803 and became a French trade man.
Earl St Vincent was a British ship captured in 1803 and became a French trade man.
---------------------------------------------------------
```

```
Enter text to paraphrase: I am a man.
Generating outputs:   0%|          | 0/1 [00:00<?, ?it/s]
---------------------------------------------------------
I am a man.

Predictions >>>
I am a man.
I am a man.
I am a man.
---------------------------------------------------------
```


## Training Logs

```
INFO:filelock:Lock 140619646915664 acquired on /root/.cache/huggingface/transformers/f5310d276a6d1648d00c32fadc8bf7b4607e0fbd5b404fc4a0045960aa2bdfdb.8512cdf8592f538a7fd4b40eecaa096285410ec6494049568b3300922ab71165.lock
Downloading:   0%|          | 0.00/1.63k [00:00<?, ?B/s]
INFO:filelock:Lock 140619646915664 released on /root/.cache/huggingface/transformers/f5310d276a6d1648d00c32fadc8bf7b4607e0fbd5b404fc4a0045960aa2bdfdb.8512cdf8592f538a7fd4b40eecaa096285410ec6494049568b3300922ab71165.lock
INFO:filelock:Lock 140619646551248 acquired on /root/.cache/huggingface/transformers/486355ec722ef05fd480e999d4c763be56549ae930f6a3742ee721a5d2a05647.9faea28a6782a9589c09b1942c039943df02232d83d2ac288a69ddfa928eae22.lock
Downloading:   0%|          | 0.00/558M [00:00<?, ?B/s]
INFO:filelock:Lock 140619646551248 released on /root/.cache/huggingface/transformers/486355ec722ef05fd480e999d4c763be56549ae930f6a3742ee721a5d2a05647.9faea28a6782a9589c09b1942c039943df02232d83d2ac288a69ddfa928eae22.lock
INFO:filelock:Lock 140619646903248 acquired on /root/.cache/huggingface/transformers/43978bdeaa326572886b44fcfed82f932f76571095ce31973e51c3da8ccade7f.d67d6b367eb24ab43b08ad55e014cf254076934f71d832bbab9ad35644a375ab.lock
Downloading:   0%|          | 0.00/899k [00:00<?, ?B/s]
INFO:filelock:Lock 140619646903248 released on /root/.cache/huggingface/transformers/43978bdeaa326572886b44fcfed82f932f76571095ce31973e51c3da8ccade7f.d67d6b367eb24ab43b08ad55e014cf254076934f71d832bbab9ad35644a375ab.lock
INFO:filelock:Lock 140619646976656 acquired on /root/.cache/huggingface/transformers/3c167ed8af56e6605eeb794b63a79d65d85e6708c9b04408d41946337030f5cd.5d12962c5ee615a4c803841266e9c3be9a691a924f72d395d3a6c6c81157788b.lock
Downloading:   0%|          | 0.00/456k [00:00<?, ?B/s]
INFO:filelock:Lock 140619646976656 released on /root/.cache/huggingface/transformers/3c167ed8af56e6605eeb794b63a79d65d85e6708c9b04408d41946337030f5cd.5d12962c5ee615a4c803841266e9c3be9a691a924f72d395d3a6c6c81157788b.lock
INFO:filelock:Lock 140619646726224 acquired on /root/.cache/huggingface/transformers/a878fcd69bba037c9b1b227f4213579ae43d0aaa9374e167bc6c5f41b1cfeb30.fc9576039592f026ad76a1c231b89aee8668488c671dfbe6616bab2ed298d730.lock
Downloading:   0%|          | 0.00/1.36M [00:00<?, ?B/s]
INFO:filelock:Lock 140619646726224 released on /root/.cache/huggingface/transformers/a878fcd69bba037c9b1b227f4213579ae43d0aaa9374e167bc6c5f41b1cfeb30.fc9576039592f026ad76a1c231b89aee8668488c671dfbe6616bab2ed298d730.lock
INFO:simpletransformers.seq2seq.seq2seq_utils: Creating features from dataset file at cache_dir/
  0%|          | 0/10000 [00:00<?, ?it/s]
INFO:simpletransformers.seq2seq.seq2seq_model: Training started
Epoch:   0%|          | 0/1 [00:00<?, ?it/s]
Finishing last run (ID:33alu3n5) before initializing another...

Waiting for W&B process to finish, PID 1539
Program ended successfully.
VBox(children=(Label(value=' 0.00MB of 0.00MB uploaded (0.00MB deduped)\r'), FloatProgress(value=1.0, max=1.0)…
Find user logs for this run at: /content/wandb/run-20210813_214141-33alu3n5/logs/debug.log
Find internal logs for this run at: /content/wandb/run-20210813_214141-33alu3n5/logs/debug-internal.log
Run summary:

Training loss	0.42822
lr	0.0
global_step	1250
_runtime	1200
_timestamp	1628892102
_step	24
Run history:

Training loss	█▅▅▄▂▃▄▄▃▃▃▃▅▄▄▄▃▄▅▃▂▃▃▁▂
lr	▆██▇▇▇▆▆▆▆▅▅▅▄▄▄▃▃▃▃▂▂▂▁▁
global_step	▁▁▂▂▂▂▃▃▃▄▄▄▅▅▅▅▆▆▆▇▇▇▇██
_runtime	▁▁▂▂▂▂▃▃▃▄▄▄▄▅▅▅▆▆▆▇▇▇▇██
_timestamp	▁▁▂▂▂▂▃▃▃▄▄▄▄▅▅▅▆▆▆▇▇▇▇██
_step	▁▁▂▂▂▂▃▃▃▄▄▄▅▅▅▅▆▆▆▇▇▇▇██

Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)

Synced exalted-oath-7: https://wandb.ai/wandbvision/Paraphrasing%20with%20BART/runs/33alu3n5
...Successfully finished last run (ID:33alu3n5). Initializing new run:

huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)
2021-08-13 22:30:51.210215: I tensorflow/stream_executor/platform/default/dso_loader.cc:53] Successfully opened dynamic library libcudart.so.11.0
Tracking run with wandb version 0.12.0
Syncing run faithful-thunder-8 to Weights & Biases (Documentation).
Project page: https://wandb.ai/wandbvision/Paraphrasing%20with%20BART
Run page: https://wandb.ai/wandbvision/Paraphrasing%20with%20BART/runs/129xl0ul
Run data is saved locally in /content/wandb/run-20210813_223043-129xl0ul

Running Epoch 0 of 1:   0%|          | 0/1250 [00:00<?, ?it/s]
INFO:simpletransformers.seq2seq.seq2seq_model:Saving model into outputs/checkpoint-1250-epoch-1
INFO:simpletransformers.seq2seq.seq2seq_utils: Creating features from dataset file at cache_dir/
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)
  0%|          | 0/3539 [00:00<?, ?it/s]
INFO:simpletransformers.seq2seq.seq2seq_model:{'eval_loss': 0.6753060039099272}
INFO:simpletransformers.seq2seq.seq2seq_model:Saving model into outputs/best_model
INFO:simpletransformers.seq2seq.seq2seq_model:Saving model into outputs/
INFO:simpletransformers.seq2seq.seq2seq_model: Training of facebook/bart-base model complete. Saved to outputs/.
Generating outputs:   0%|          | 0/222 [00:00<?, ?it/s]
```
