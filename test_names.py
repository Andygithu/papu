from names import make_full_name,extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name('Sally','Brown-Arellano') == 'Brown-Arellano;Sally'
    assert make_full_name('Andy','Arellano') == 'Arellano;Andy'
    assert make_full_name('','') == ';'
    assert make_full_name('Liliana','Choez') == 'Choez;Liliana'

def test_extract_family_name():
    assert extract_family_name('Brown-Arellano;Sally') == 'Brown-Arellano'
    assert extract_family_name('Arellano;Andy') == 'Arellano'
    assert extract_family_name('Draper;Amanda') == 'Draper'
    assert extract_family_name(';') == ''

def test_extract_given_name():
    assert extract_given_name('Brown-Arellano;Sally') == 'Sally'
    assert extract_given_name('Arellano;Andy') == 'Andy'





pytest.main(["-v", "--tb=line", "-rN", __file__])