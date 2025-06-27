# prepare data for finetuning
# load pretrained tokenizer, call it with dataste -> EncodingWarning
# build pytorch dataset with encodings
# load pretrained model
# load trainer and train int
# native pytorch training loop

from transformers import Trainer, TrainingArguments

training_Args = TrainingArguments("test_trainer")

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)

trainer.train()