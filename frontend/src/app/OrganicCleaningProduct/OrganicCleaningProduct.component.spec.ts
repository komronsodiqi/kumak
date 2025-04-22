import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrganicCleaningProductComponent } from './OrganicCleaningProduct.component';

describe('organicCleaningProductComponent', () => {
  let component: OrganicCleaningProductComponent;
  let fixture: ComponentFixture<OrganicCleaningProductComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OrganicCleaningProductComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OrganicCleaningProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
