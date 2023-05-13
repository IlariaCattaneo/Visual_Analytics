## Using conda environment with jupyter kernels

First you need to define your conda environment. For that you can use the vaa.yml file that you can download from icorsi. The file provides the name of the environment and its dependencies.

To create the environment, assuming you already installed conda:
```
$ conda env create -f vaa.yml
```

This command will resolve and download all the dependencies and will associate them with the environment. Environments are sandboxed from one another, so that you will not have dependency conflics, which in python are not fun to resolve.
Once the environment is created, you can activate and deactivate it with the corresponding conda command, using the name of the environment as defined in the yml file.

```
$ conda activate visual-analytics
```

If you use [ohmyz](https://ohmyz.sh/), similarly to the git branch features, it will show you the current environment.

Once your conda environment is active, with all the dependencies available, you can register it as a ipython kernel, to be used in Jupyter. This will ensure that you have your dependencies in Jupyter while not conflicting with other python environment you might have.

To register the kernel run the following command:

```
python -m ipykernel install --user --name "<PICK A KERNEL NAME>" --display-name "<NAME THAT WILL APPEAR IN JUPYTER>"
```

