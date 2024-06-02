
output=snap/sp/baseline
PYTHONPATH=$PYTHONPATH:./src \
python -m torch.distributed.launch \
    --nproc_per_node=$1 \
    VLModel/src/vsd.py \
        --distributed --multiGPU \
        --train train \
        --valid val \
        --test test \
        --optim adamw \
        --warmup_ratio 0.1 \
        --clip_grad_norm 5 \
        --lr 5e-5 \
        --epochs 20 \
        --num_workers 4 \
        --backbone 'google/flan-t5-base' \
        --output $output ${@:2} \
        --load ./VLModel/snap/vlt5/Epoch30 \
        --num_beams 5 \
        --batch_size 80 \
        --valid_batch_size 100 \
