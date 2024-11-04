from kubernetes.client.models import V1Pod

def pod_mutation_hook(pod: V1Pod):
    pod.metadata.name = "analytics-airflow-%s" % pod.metadata.name