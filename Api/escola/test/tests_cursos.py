from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):
    #criando um cenário de teste para nao usar os dados inseridos na API
    def setUp(self):
        self.list_urls = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso teste 1',nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT5', descricao='Curso teste 2',nivel='A'
        )
        self.curso_3 = Curso.objects.create(
            codigo_curso='CTT4', descricao='Curso teste 3',nivel='A'
        )
    #teste para falhar de proposito
    #def test_fail(self):
     #   self.fail('Failed')
    
    #Teste das requisições
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar se a requisição GET esta funcionando e listando os cursos"""
        response = self.client.get(self.list_urls)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.context['object_list']), 1)


    def test_requisicao_post_para_criar_cursos(self): 
        """Teste para verificar se a requisição POST esta funcionando e criando os cursos"""
        response = self.client.post(self.list_urls)
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_urls, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_cursos(self):
        """Teste para verificar se a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    

    def test_requisicao_put_para_atualizar_cursos(self):
        """Teste para verificar se a requisição PUT para atualizar um curso"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3 atualizado',
            'nivel': 'B'
        }
        response = self.client.put('/cursos/1/',data=data)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
        